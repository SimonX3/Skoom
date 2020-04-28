from server.brokers.video_broker import video_broker

from pickle import loads, PickleError


def main_datagram_broker(data_received_iterator):
    for datagram in data_received_iterator:
        try:
            data = loads(datagram)
            if data['datagram_type'] == 'video':
                frame = video_broker.send(data)
                if frame is not None:
                    yield ('video', frame)

            if data['datagram_type'] == 'audio':
                yield ('audio', data)
        except PickleError:
            pass

